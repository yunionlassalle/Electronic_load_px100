"""Independent manual exports; never reuse autosave names."""
from datetime import datetime
from pathlib import Path
import re


def export_trial(data, figure, label, directory, internal=None):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    label = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', label.strip())
    label = label.replace(' ', '_').rstrip('. ') or 'Prueba'
    directory = directory / label
    directory.mkdir(parents=True, exist_ok=True)
    base = label + '_' + datetime.now().strftime('%Y%m%d_%H%M%S')
    number = 0
    while True:
        name = base if number == 0 else f'{base}_{number:02d}'
        csv = directory / (name + '.csv')
        png = directory / (name + '.png')
        extra = directory / (name + '_internal_r.csv')
        if png.exists() or extra.exists():
            number += 1
            continue
        try:
            stream = csv.open('x', encoding='utf-8', newline='')
        except FileExistsError:
            number += 1
            continue
        break
    files = [csv]
    try:
        with stream:
            data.to_csv(stream, index=False)
        figure.savefig(png, dpi=150, bbox_inches='tight')
        files.append(png)
        if internal is not None and not internal.empty:
            with extra.open('x', encoding='utf-8', newline='') as output:
                internal.to_csv(output, index=False)
            files.append(extra)
    except Exception as exc:
        raise RuntimeError(f'Guardado incompleto en {directory}: {exc}. Comprueba los archivos antes de reiniciar los datos.') from exc
    return files
