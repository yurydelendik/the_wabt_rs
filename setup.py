from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(name='the_wabt_rs',
      version="0.0.1",
      classifiers=[
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Rust",
            "Operating System :: POSIX",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
      ],
      packages=["the_wabt_rs"],
      rust_extensions=[RustExtension('the_wabt_rs.lib_wabt_rs', 'Cargo.toml',  binding=Binding.PyO3)],
      zip_safe=False)
