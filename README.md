Databricks CLI Bundles
Write code once, deploy everywhere
What are Databricks Asset Bundles?
Databricks Asset Bundles are essentially YAML files that specify the code artifacts (file, notebooks, binaries), resources, and configurations of a Databricks project

To learn more, see:
* The public preview announcement at 
https://www.databricks.com/blog/announcing-public-preview-databricks-asset-bundles-apply-software-development-best-practices
* The docs at 
* DAB https://docs.databricks.com/dev-tools/bundles/index.html

* configure wrokspace access to ide
https://docs.databricks.com/en/dev-tools/cli/authentication.html

* Bundle template
https://docs.databricks.com/en/dev-tools/bundles/templates.html

* Bundle libraries dependecies
https://docs.databricks.com/en/dev-tools/bundles/library-dependencies.html

* Github Action
https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions


* setup local env - https://docs.databricks.com/en/dev-tools/cli/install.html#homebrew-install
* 1. install db cli and verify
    brew tap databricks/tap
    brew install databricks
    databricks -v 
    databricks --help

* 2. install IDE (VS code) 
* 3. setup git repo
     mkdir TEST-DAB
     git init
     echo "# TEST-DAB" >> README.md  
     git commit -am "main branch initialization" 
     git branch -M main 
     git remote add origin git@github.com:databricks/TEST-DAB.git
     git push -u origin main

* 4. setup python project using poetry
     1. install poetry if its not alreday installed
            create dir e.g. 
     2. mkdir test-dab
        cd test-dab
     3. poetry init # follow interactive promt instruction, it generates pyproject.toml file with containts followed by prompt instruction e.g.
                    Generated file

                    [tool.poetry]
                    name = "example"
                    version = "0.1.0"
                    description = ""
                    authors = ["author eamil id"]
                    readme = "README.md"

                    [tool.poetry.dependencies]
                    python = "^3.11"

                    [build-system]
                    requires = ["poetry-core"]
                    build-backend = "poetry.core.masonry.api"

     4. create source package folder  e.g. "example"
        add pyhton files/notebook and resources

     5. Create databricks.yml bundle file at root project folder refer sample template or bundle schema file
     6. validate and deploy bundle
        databricks bundle validate  -e dev
        databricks bundle deploy  -e dev
        databricks bundle run dtl_pipeline -e dev
     7. review your execution in the dev workspace

* 5.  setup ci/cd using github action https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions
     1. Add CI pipeline on PR against main branch
        create .github/workflows directory
        add dev.yml
     2. Add Databricks Workspace Token for dev in Github actions secret
     3. Add CD pipeline on PR merge on main branch
        create .github/workflows directory
        add prod.yml
     4. Add Databricks Workspace Token for PROD in Github actions secrets
     5. commit and push your changes

* 6. Create a Pull Request against the main branch. This will kick off CI ppeline. 
* 7. Review and Merge PR (CI). This will kick off the CD pipeline and your latest code will be deployed in prod.
     
* 8. Build python wheel with Poetry
    1. Prerequisites
        1. Databricks CLI v0.209.0 or above
        2. Python 3.10 or above
        3. Poetry 1.6 or above (install with `pip3 install poetry`)

    2. Update the `host` field under `workspace` in `databricks.yml` to the Databricks workspace you wish to deploy to

    3. yml section in databricks.yml will looks as below e.g.
       workspace:
        host: https://dbc-a49c6081-8a5a.cloud.databricks.com/

        artifacts:
            default:
                type: whl
                build: poetry build
* 9. Define entry point for build inside pyproject.toml file e.g.
        The `pyproject.toml` file in the root of this bundle refers to this function as an entry point in the [tool.poetry.scripts] section.
        [tool.poetry.scripts]
        example = "example.main:main"  here example "name" key defined .toml file and its package name and main is python file contains entry point function/def is main where my process gets start.

* 10. setup ci/cd config with github action at .github/workflows/ yml file
      1. add trigger when to run ci/cd pipeline e.g. on push/workflow_dispatch when head brahcn gets updated
      2. setup deployment steps. e.g. setting up vm, build packages cli etc
      3. validate , deploy and run the bundle

      e.g. setting up python and poetry on vm  - refer https://github.com/marketplace?type=actions for more details and options
      # setup python version
      - uses: actions/setup-python@v4
        with:
          python-version: 3.11
      # setup poetry
      - name: Run image
        uses: abatilo/actions-poetry@v2
        with:
          poetry-version: 1.7.0

