from src.models import AssetSpecInput, AssetComplianceReport

class GameAssetGovernorSkill:
    """A Custom AI Skill that enforces game engine and interactive platform budgets

    across studio development pipelines (Console, Mobile, Cloud Gaming).
    """
    ENGINE_BUDGETS = {
        "Mobile": {"max_vram_mb": 64.0, "max_poly": 25000, "max_draw_calls": 80},
        "Web": {"max_vram_mb": 128.0, "max_poly": 50000, "max_draw_calls": 120},
        "Cloud_Gaming": {"max_vram_mb": 256.0, "max_poly": 100000, "max_draw_calls": 250},
        "Console": {"max_vram_mb": 512.0, "max_poly": 250000, "max_draw_calls": 500}
    }

    def evaluate_asset(self, asset: AssetSpecInput) -> AssetComplianceReport:
        platform = asset.target_platform if asset.target_platform in self.ENGINE_BUDGETS else "Console"
        budget = self.ENGINE_BUDGETS[platform]
        
        violations = []
        recommendations = []

        if asset.texture_memory_mb > budget["max_vram_mb"]:
            diff = asset.texture_memory_mb - budget["max_vram_mb"]
            violations.append(f"Texture VRAM exceeded by {diff:.1f}MB (Max allowed: {budget['max_vram_mb']}MB)")
            recommendations.append("Apply texture mip-mapping compression (BC7/ASTC) and downsample 4K textures to 2K.")

        if asset.draw_calls > budget["max_draw_calls"]:
            diff = asset.draw_calls - budget["max_draw_calls"]
            violations.append(f"Draw calls exceed budget by {diff} (Max allowed: {budget['max_draw_calls']})")
            recommendations.append("Batch static meshes and combine material texture atlases.")

        if asset.poly_count > budget["max_poly"]:
            diff = asset.poly_count - budget["max_poly"]
            violations.append(f"Polygon count exceeded by {diff:,} triangles")
            recommendations.append("Generate Level-of-Detail (LOD) hierarchies for distance culling.")

        compliant = len(violations) == 0

        return AssetComplianceReport(
            asset_id=asset.asset_id,
            target_platform=platform,
            compliant=compliant,
            budget_violations=violations,
            optimization_recommendations=recommendations,
            approved_engine_contract={
                "asset_id": asset.asset_id,
                "status": "APPROVED" if compliant else "REJECTED_GATED",
                "allocated_vram_mb": min(asset.texture_memory_mb, budget["max_vram_mb"]),
                "lod_generation_required": not compliant
            }
        )
