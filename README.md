The flow:

1. By default, the `v1` and `dev` branches are built automatically with ReadTheDocs
2. The `v1` branch corresponds to the `stable` doc version, `dev` corresponda to `dev`
3. Develop and refactor in the `dev` branch, then merge into `v1` to get a `stable` version
4. Create branches as you see fit when developing features, and activate a corresponding **_hidden_** version on the [RedTheDocs](https://readthedocs.org/projects/soveren/versions/) if you need visualization and don't want to bother with local setup
