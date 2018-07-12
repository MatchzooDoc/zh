import os
import sys
language=sys.argv[1]
option=sys.argv[2]
root_dir =os.path.dirname(os.path.realpath(__file__))
Matchzoo_path=os.path.join(root_dir,'MatchZoo')
matchzoo_path=os.path.join(Matchzoo_path,'matchzoo')
doc_path=os.path.join(root_dir,'docs')
if option=='fbuild':#first build
    os.system('git config http.postBuffer 524288000')
    os.system('git submodule add https://github.com/faneshion/MatchZoo')
    os.chdir(Matchzoo_path)
    os.system('git checkout 2.0')
    os.chdir(doc_path)
    os.system('sphinx-apidoc -o ./source '+matchzoo_path)
    os.system('make gettext')
    os.system('sphinx-intl update -p _build/gettext -l '+language)
    os.system('sphinx-intl build')
    os.system('sphinx-intl stat')
    os.system('''make -e SPHINXOPTS="-D language='{}'" html'''.format(language))
elif option=='update':
    os.chdir(doc_path)
    os.system('sphinx-intl build')
    os.system('sphinx-intl stat')
    os.system('make clean')
    os.system('''make -e SPHINXOPTS="-D language='{}'" html'''.format(language))
elif option=='rebuild':#main project update
    os.chdir(root_dir)
    os.system('git submodule update --remote')
    os.chdir(doc_path)
    os.system('sphinx-apidoc -f -o ./source ' + matchzoo_path)
    os.system('make gettext')
    os.system('sphinx-intl update -p _build/gettext -l ' + language)
    os.system('sphinx-intl build')
    os.system('sphinx-intl stat')
    os.system('''make -e SPHINXOPTS="-D language='{}'" html'''.format(language))