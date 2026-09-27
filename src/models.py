from pydantic import BaseModel, Field
from typing import List, Optional

class AssetSpecInput(BaseModel):
    asset_id: str
    name: str
    target_platform: str  # 'Mobile', 'Console', 'Web', 'Cloud_Gaming'
    texture_memory_mb: float
    poly_count: int
    draw_calls: int
    interactive_sync_rate_hz: int

class AssetComplianceReport(BaseModel):
    asset_id: str
    target_platform: str
    compliant: bool
    budget_violations: List[str]
    optimization_recommendations: List[str]
    approved_engine_contract: dict
