from enum import Enum

class CropFamily(str, Enum):
    GRAMINEAE = "Gramíneas (Cereales)"
    LEGUMINOSAE = "Leguminosas (Fijadoras de Nitrógeno)"
    CUCURBITACEAE = "Cucurbitáceas"
    SOLANACEAE = "Solanáceas"
    MALVACEAE = "Malváceas"