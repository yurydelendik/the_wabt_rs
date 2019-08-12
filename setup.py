from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(name='lib_wabt_rs',
      version="0.0.1",
      rust_extensions=[RustExtension('lib_wabt_rs', 'Cargo.toml',  binding=Binding.PyO3)],
      zip_safe=False)
