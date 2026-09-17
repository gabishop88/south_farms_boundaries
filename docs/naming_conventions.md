# Naming Conventions

These are the rules that describe how files are named in this project.

Unless otherwise specified, the default capitalization scheme should be snake_case, which is characterized by all lower case letters separating words with underscores.

## Common Attributes

| attribute | description | values | example |
| --------- | ----------- | ------ | ------- |
| `descriptor` | This is a discretionary attribute where you try to include as short a description of the purpose of the file as possible. | anything | `naming_conventions.md`
| `method`    | How data was acquired. Could  be downloaded from Operations Center (deere) or collected manually. | `deere_`, `collected_` | `collected_soyface.pdf` |
| `farm` | This is which farm in the south farms the data pertains to. | `alma_plots`, `burwash_farm`, `energy_farm`, `fisher_farm`, `maxwell_farm`, `maxwell_trust`, `soyface`, ... | `collected_maxwell_trust.pdf` |

## Documentation

* `.md` files can be named as one word in all caps, such as `README.md` for files that are known to use that format, as with README. Otherwise, they should simply be a `descriptor`, such as `naming_conventions.md`.
* maps should be `.pdf` files named with the `method` and `farm`, like `collected_soyface.pdf`.
