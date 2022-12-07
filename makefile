override PACKAGE = openai_model
override CONDA_BASE = /Users/zhans/miniconda3
override CONDA =  ${CONDA_BASE}/bin/conda
override PIP =  ${CONDA_BASE}/bin/pip3
override CONDA_ENV_PATH = /tmp/opt/$(PACKAGE)
override GIT_TAG    = $$(git describe --always --tags $$(git rev-list --tags --max-count=1))
override GIT_NUMBER = $$(git rev-list --count HEAD ^$(GIT_TAG))
override TAG_LOCAL = openai_model
override TAG_ECR = 839525146093.dkr.ecr.ap-southeast-2.amazonaws.com/openai_model:latest
override PLATFORM = osx-arm64

# ------------
# PLATFORM: osx-arm64 OR linux-64
# ------------

conda_remove_build:
	rm -rf $(CONDA_ENV_PATH)
	rm -rf $(CONDA_BASE)/pkgs/$(PACKAGE)*
	rm -rf $(CONDA_BASE)/conda-bld/$(PLATFORM)/$(PACKAGE)*
	rm -rf $(CONDA_BASE)/conda-bld/$(PACKAGE)*
	rm -rf $(CONDA_BASE)/conda-bld/$(PLATFORM)/.cache/paths/$(PACKAGE)*
	rm -rf $(CONDA_BASE)/conda-bld/$(PLATFORM)/.cache/index/$(PACKAGE)*
	rm -rf $(CONDA_BASE)/conda-bld/$(PLATFORM)/.cache/recipe/$(PACKAGE)*
	$(CONDA) index $(CONDA_BASE)/conda-bld

conda_build: conda_remove_build
	GIT_DESCRIBE_TAG=$(GIT_TAG) GIT_DESCRIBE_NUMBER=$(GIT_NUMBER) $(CONDA) build . --no-test -c conda-forge

conda_create_env:
	mkdir -p /tmp/opt
	$(CONDA) create -p $(CONDA_ENV_PATH) -y

conda_install:
	$(CONDA) install $(PACKAGE) -y -p $(CONDA_ENV_PATH) -c local -c conda-forge --force-reinstall 

install: conda_build conda_create_env conda_install


