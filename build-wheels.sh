#!/bin/bash
set -ex

curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain nightly  -y
export PATH="$HOME/.cargo/bin:$HOME/.cmake/bin:$PATH"

for PYBIN in /opt/rh/rh-python36/root/usr/bin; do
    export PYTHON_SYS_EXECUTABLE="$PYBIN/python"
    sudo "${PYBIN}/pip" install -U pip setuptools wheel==0.31.1 setuptools-rust auditwheel
    "${PYBIN}/python" setup.py bdist_wheel
done

export PATH="/opt/rh/rh-python36/root/usr/bin:$PATH"
for whl in dist/*.whl; do
    auditwheel repair "$whl" -w dist/
done

mkdir wheelhouse
mv dist/*.whl wheelhouse/
