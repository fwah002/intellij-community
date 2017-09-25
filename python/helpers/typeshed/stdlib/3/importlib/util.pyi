import importlib.abc
import importlib.machinery
import sys
import types
from typing import Any, Callable, List, Optional

def module_for_loader(
    fxn: Callable[..., types.ModuleType]
) -> Callable[..., types.ModuleType]: ...
def set_loader(
    fxn: Callable[..., types.ModuleType]
) -> Callable[..., types.ModuleType]: ...
def set_package(
    fxn: Callable[..., types.ModuleType]
) -> Callable[..., types.ModuleType]: ...

if sys.version_info >= (3, 3):
    def resolve_name(name: str, package: str) -> str: ...

if sys.version_info >= (3, 4):
    MAGIC_NUMBER = ...  # type: bytes

    def cache_from_source(path: str, debug_override: Optional[bool] = None, *,
                          optimization: Optional[Any] = None) -> str: ...
    def source_from_cache(path: str) -> str: ...
    def decode_source(source_bytes: bytes) -> str: ...
    def find_spec(
        name: str, package: Optional[str] = None
    ) -> importlib.machinery.ModuleSpec: ...
    def spec_from_loader(
        name: str, loader: Optional[importlib.abc.Loader], *,
        origin: Optional[str] = None, loader_state: Optional[Any] = None,
        is_package: Optional[bool] = None
    ) -> importlib.machinery.ModuleSpec: ...
    def spec_from_file_location(
        name: str, location: str, *,
        loader: Optional[importlib.abc.Loader] = None,
        submodule_search_locations: Optional[List[str]] = None
    ) -> importlib.machinery.ModuleSpec: ...

if sys.version_info >= (3, 5):
    def module_from_spec(
        spec: importlib.machinery.ModuleSpec
    ) -> types.ModuleType: ...

    class LazyLoader(importlib.abc.Loader):
        def __init__(self, loader: importlib.abc.Loader) -> None: ...
        @classmethod
        def factory(
            cls, loader: importlib.abc.Loader
        ) -> Callable[..., 'LazyLoader']: ...
        def create_module(
            self, spec: importlib.machinery.ModuleSpec
        ) -> Optional[types.ModuleType]: ...
        def exec_module(self, module: types.ModuleType) -> None: ...
