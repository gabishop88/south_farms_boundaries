# South Farms Boundaries

This is a repository of boundaries for the UIUC South Farms. It contains boundaries that are manually collected as well as generated ones from John Deere's Operations Center.

The naming conventions used in this project can be found in [naming_conventions.md](./docs/naming_conventions.md)

## Available Files
> TODO: Add file tree once I have everything together.

## Point Collection

The data in `data/raw_points` was collected directly using an EMLID Rover and using a base station on campus. When collecting, an accuracy of 2.5cm was required before collecting a point. Each point was collected after acquiring a satellite fix and was averaged over collecting multiple points in quick succession.

> TODO: Finish including collection details. Specifically, detail all of the settings used in the app and how to set up a project, collect points, and export it.

## Polygon Generation

The data in `data/collected_polygons` was generated using the collected points in QGIS. Detailed instructions on multiple methods to generate these polygons can be found in [points_to_poly.md](./docs/points_to_poly.md)
