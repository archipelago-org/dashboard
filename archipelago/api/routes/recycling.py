from fastapi import APIRouter
from archipelago.models.co2_reduction import Co2Reduction
from archipelago.models.recycling_efficiency import RecyclingEfficiency
from archipelago.services.recycling_service import RecyclingService

router = APIRouter()


@router.get("/co2-reduction", response_model=Co2Reduction, name="co2_reduction")
def get_co2_reduction() -> Co2Reduction:
    return RecyclingService().get_co2_reduction()


@router.get("/efficiency", response_model=RecyclingEfficiency, name="efficiency")
def get_efficiency() -> RecyclingEfficiency:
    efficiency = RecyclingEfficiency(
        sequestration_efficiency=99.8)  # TODO: add actual calculation
    return efficiency
