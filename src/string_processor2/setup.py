import Cython.Distutils
import distutils.core
import os

include_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
include_dir = os.path.join(include_dir, "lib")
print include_dir

distutils.core.setup(
        name="string_processor",
        cmdclass={
            "build_ext": Cython.Distutils.build_ext,
        },
        ext_modules=[
            distutils.extension.Extension(
                "string_processor",
                ["string_processor.pyx"],
                libraries=["stringprocessor"],
                include_dirs=[include_dir],
                library_dirs=[include_dir],
            ),
        ],
)
