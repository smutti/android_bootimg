#!/usr/bin/env python

import argparse
import sys
import subprocess
from shutil import copy, rmtree
from os import listdir, makedirs, chdir, getcwd, walk
from os.path import isdir, isfile, join, exists, abspath, dirname

prebuilts_dir='prebuilts'

def unpack_boot(bootimg, base_dir, tmp_dir):

    mkboot = join(join(base_dir, prebuilts_dir), 'mkboot')
    p = subprocess.Popen([mkboot, bootimg, tmp_dir])
    p.communicate()
    return map(lambda x:join(tmp_dir, x), [name for name in listdir(tmp_dir)
            if isdir(join(tmp_dir, name))])[0]

def repack_boot(base_dir, tmp_dir, out):
    mkboot = join(join(base_dir, prebuilts_dir), 'mkboot')
    p = subprocess.Popen([mkboot, tmp_dir, join(out, 'newboot.img')])
    p.communicate()

def unpack_repack(bootimg, base_dir, tmp_dir, out, sepolicy):

    ramdisk_dir = unpack_boot(bootimg, base_dir, tmp_dir)
    
    #copy sepolicy
    copy(sepolicy, ramdisk_dir)

    repack_boot(base_dir, tmp_dir, out)


def update_boot(args):

    project_dir = dirname(abspath(__file__))
    tmp_dir = join(project_dir, 'tmp')

    if exists(tmp_dir):
        rmtree(tmp_dir)

    if exists(args.out_dir):
        rmtree(args.out_dir)
    
    makedirs(args.out_dir)

    unpack_repack(args.bootimg, project_dir, tmp_dir, args.out_dir, args.sepolicy)
    rmtree(tmp_dir)

def main():
    parser = argparse.ArgumentParser(description=__doc__)

    parser = argparse.ArgumentParser(description='Unpack and repack boot.img')
    parser.add_argument('-boot', required=True, dest='bootimg', help='boot.img file')
    parser.add_argument('-sepolicy', required=True, dest='sepolicy', 
                        help='new sepolicy file to add in the boot.img')
    parser.add_argument('-file_contexts', required=False, dest='file_contexts', 
                        help='new file_contexts file to add in the boot.img')
    parser.add_argument('-seapp_contexts', required=False, dest='seapp_contexts', 
                        help='new seapp_contexts file to add in the boot.img')
    parser.add_argument('-property_contexts', required=False, dest='property_contexts', 
                        help='new property_contexts file to add in the boot.img')
    parser.add_argument('-out', required=True, dest='out_dir', help='output directory')
    parser.set_defaults(func=update_boot)
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()