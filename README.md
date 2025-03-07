Clustering flow cytometry data
In this lab we will use k-means and hierarchical clustering on a flow cytometry dataset from a healthy control sample, from the paper "Longitudinal immune profiling reveals key myeloid signatures associated with COVID-19" (available from https://www.science.org/doi/full/10.1126/sciimmunol.abd6197).

We have only selected a small subset of the data so that we can easily visualise the clusters. In a real application we would be clustering many more cells and cell-types and dealing with variation across subjects.

In most applications of clustering there is no "ground truth" but for the purposes of this lab we have cell labels obtained from manually gating the cytometry data based on expert knowledge of the cell-type markers included in the panel. Such ground truth knowledge is only available in some cases and may contain errors. In other high-dimensional single-cell datasets clustering is often used to discover a priori unknown cell-types in a purely data-driven way.

Below we show how to get the data into your notebook.

See https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation for different approaches to assessing the performance of clustering with or without ground truth labels.
