from distutils.core import setup

setup(
    name='py_wizard',
    version='2.0',
    author='Nathan Shearer',
    author_email='shearern@gmail.com',
    package_dir={'': 'src', },
    packages=[
        'py_wizard',
        'py_wizard.console_wiz_iface',
        'py_wizard.questions',
        'py_wizard.tk_wizard_iface',
        ],
    )
