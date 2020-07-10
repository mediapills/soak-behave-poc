# Definition

The **Given-When-Then** formula is a template intended to guide the writing of acceptance tests for a **User Story**:

  **(Given)** some context
  
  **(When)** some action is carried out

  **(Then)** a particular set of observable consequences should obtain


## An example:

  Given my bank account is in credit, and I made no withdrawals recently,

  When I attempt to withdraw an amount less than my card’s limit,

  Then the withdrawal should complete without errors or warnings

## Basic usage

This will sdist-package your current project, create two virtualenv Environments, install the sdist-package into the environments and run the specified command in each of them. With:

```shell script
$ tox -e behave
```
or
```shell script
$ make behave
```

> If you want to run a single test for that feature, use the **-n** or **--name** flag which seems to want the text after **Scenario**:
> ```sh
> $ behave -n 'This is a scenario name'
> ```
> You can run a feature file by using **-i** or **--include** flags and then the name of the feature file.
> ```sh
> behave -i file_name.feature
> ```
> or
> ```sh
> behave --include file_name
> ```
