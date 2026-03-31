"""
Image Manager: Intelligent fallback mapping for missing images.
Maps requested images to available ones for graceful degradation.
"""
from pathlib import Path

# Mapping: requested_filename -> list of fallback filenames (in priority order)
IMAGE_FALLBACK_MAP = {
    # Pipeline 2
    "fuzzy_score_dist_pipe2.png": [
        "fuzzy_score_dist_pipe2.png",  # First try the exact name
        "roc_curve_pipe2.png",  # Fallback to ROC curve
    ],
    
    # Pipeline 3 - Univariate analysis
    "violin_Total_Follicles.png": [
        "violin_Total_Follicles.png",
        "metrics_comparison_pipe3.png",  # Fallback: metric comparisons
        "KNN_summary_pipe3.png",
    ],
    "violin_LH_FSH_Ratio.png": [
        "violin_LH_FSH_Ratio.png",
        "metrics_comparison_pipe3.png",
        "ANN_summary_pipe3.png",
    ],
    
    # Pipeline 3 - Clustering
    "pca_clusters_pipe3.png": [
        "pca_clusters_pipe3.png",
        "ANN_summary_pipe3.png",  # ANN models often visualize clusters
        "NaiveBayes_summary_pipe3.png",
        "KNN_summary_pipe3.png",
    ],
}


def resolve_image(filename: str) -> Path | None:
    """
    Resolve an image to an existing file, using fallback mapping.
    Returns the first file that exists from the fallback chain.
    """
    # Get fallback chain for this filename, default to just the filename itself
    fallback_chain = IMAGE_FALLBACK_MAP.get(filename, [filename])
    
    for candidate in fallback_chain:
        # Try in images/ folder first
        images_path = Path("images") / candidate
        if images_path.exists():
            return images_path
        
        # Try in root
        root_path = Path(candidate)
        if root_path.exists():
            return root_path
    
    return None
