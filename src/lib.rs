use pyo3::exceptions::Exception;
use pyo3::prelude::*;
use pyo3::types::{PyBytes, PyString};
use pyo3::wrap_pyfunction;

use wabt;

#[pyfunction]
pub fn wat2wasm<'p>(py: Python<'p>, wat: &PyString) -> PyResult<&'p PyBytes> {
    let wat = wat.to_string()?;
    let wasm = wabt::wat2wasm(&wat.as_bytes())
        .map_err(|_| PyErr::new::<Exception, _>("wat2wasm error"))?;
    Ok(PyBytes::new(py, &wasm))
}

#[pymodule]
fn lib_wabt_rs(_: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(wat2wasm))?;
    Ok(())
}
