.PHONY : all
all:
	jupyter execute index.ipynb
    
.PHONY : env
env:
    conda env create -f environment.yml

.PHONY : html
html:
    jupyterbook build .


.PHONY : html-hub
html-hub:
    jupyter-book config sphinx .
    sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
    python -m _build/html/http.server


.PHONY : clean
clean :
	rm -f audio/*.wav
	rm -f figures/*.png
    jupyter-book clean ../homework6