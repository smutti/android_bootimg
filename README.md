# android_bootimg

Python utility for unpack, modify and repack an android boot image.

The utility support the modification (i.e., overwrite) of the following files:
- sepolicy
- file_contexts
- seapp_contexts
- property_contexts

## How to use it
---
**from the command line**:

    python bootimg.py -boot path/to/boot.img -out path/to/out_dir

optionally you can specify the files to overwrite:

*overwrite sepolicy*

    python bootimg.py -boot path/to/boot.img -sepolicy path/to/sepolicy -out path/to/out_dir

*overwrite file_contexts*

    python bootimg.py -boot path/to/boot.img -sepolicy path/to/file_contexts -out path/to/out_dir

*overwrite seapp_contexts*

    python bootimg.py -boot path/to/boot.img -sepolicy path/to/seapp_contexts -out path/to/out_dir

*overwrite property_contexts*

    python bootimg.py -boot path/to/boot.img -sepolicy path/to/property_contexts -out path/to/out_dir


This is a work in progress.  Please give feedback!
