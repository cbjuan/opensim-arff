# opensim-arff
Scripts to produce ARFF files (Weka) from Opensim's database and logs. 
This code uses to Opensim.log and Robust.log to extract info about teleports, sessions, etc.
Also, the code uses a MySQL connection to gather data about users, terrains, user groups, etc.

All the info is saved in JSON files. Some data are also stored in ARFF files (valid for [Weka](https://www.cs.waikato.ac.nz/ml/weka/) software) to be used in data mining algorithms and processes.

## Academic works related

This software has been used as part of the following academic papers. If you use it, please cite any of them or the repo itself.

 * Cruz-Benito, J., Therón, R., Pizarro, E., & García-Peñalvo, F. J. (2013, November). Knowledge discovery in virtual worlds usage data: approaching web mining concepts to 3D virtual environments. In Proceedings fourth international workshop on knowledge discovery, knowledge management and decision support (Eureka-2013). [PDF](http://hdl.handle.net/10366/122588)
 * Cruz-Benito, J., Therón-Sánchez, R., & Pizarro Lucas, E. (2013). Soluciones visuales interactivas aplicadas a grandes volúmenes de datos de entornos 3D de aprendizaje y prácticas. [PDF](https://gredos.usal.es/jspui/bitstream/10366/122490/1/DIA_HEBATT_Paper_JuanCB_LibroMaster.pdf)
 * Cruz-Benito, J., Therón, R., Pizarro, E., & García-Peñalvo, F. J. (2013, September). Análisis de datos en mundos virtuales educativos. In Actas del XV Simposio Internacional de Tecnologías de la Información y las Comunicaciones en la Educación (SINTICE13). [PDF](https://repositorio.grial.eu/bitstream/grial/269/1/sintice2013.pdf)
 * Cruz-Benito, J., Sánchez, R. T., García-Peñalvo, F. J., & Lucas, E. P. (2013, November). Analyzing users' movements in virtual worlds: discovering engagement and use patterns. In Proceedings of the First International Conference on Technological Ecosystem for Enhancing Multiculturality (pp. 559-564). ACM. DOI: [10.1145/2536536.2536622](https://doi.org/10.1145/2536536.2536622)
 * Cruz-Benito, J., Therón, R., García-Peñalvo, F. J., & Lucas, E. P. (2015). Discovering usage behaviors and engagement in an Educational Virtual World. Computers in Human Behavior, 47, 18-25. DOI: [10.1016/j.chb.2014.11.028](https://doi.org/10.1016/j.chb.2014.11.028)

To check out my other papers on virtual worlds, HCI, etc., visit my [Google Scholar profile](https://scholar.google.es/citations?user=_mLnQPgAAAAJ&hl=es)

## How to cite this repo
[![DOI](https://zenodo.org/badge/107381598.svg)](https://zenodo.org/badge/latestdoi/107381598)
 * Juan Cruz-Benito. (2013). opensim-arff: scripts to produce ARFF files (Weka) from Opensim's database and logs. Zenodo. [http://doi.org/10.5281/zenodo.1019165](http://doi.org/10.5281/zenodo.1019165)

## Disclaimer 
This software was developed back in 2013 as part of my Master thesis project. It was tested with the Opensim versions available at this time. Use it carefully.


## License

    MIT License
    
    Copyright (c) 2013 Juan Cruz-Benito (juancb)
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
