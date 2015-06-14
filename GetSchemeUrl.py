#!/usr/bin/env python
#
# Scan IPA file and parse its Info.plist and report the SchemeUrl result.
#
# Copyright (c) 2015 by Ruozi,Pinssible. All rights reserved.

import zipfile
import os
import sys
import re
import plistlib

class GetSchemeUrl:

    plist_file_rx = re.compile(r'Payload/.+?\.app/Info.plist$')
    schemeurl_key_rx = re.compile(r'CFBundleURLSchemes')
	
    def __init__(self,ipa_filename):
        self.ipa_filename = ipa_filename
	
    def get_filename_from_ipa(self):
        zip_obj = zipfile.ZipFile(self.ipa_filename, 'r')
        regx = GetSchemeUrl.plist_file_rx
        filenames = zip_obj.namelist()
        filename = ''
        for fname in filenames:
            if regx.search(fname):
                filename = fname
                break

        return {'filename':filename, 'zip_obj': zip_obj}

    def extract_scheme_url(self):
        ipa_file = self.get_filename_from_ipa()

        ipa_file = getter.get_filename_from_ipa()
        plist_filename = ipa_file['filename']
        zip_obj = ipa_file['zip_obj']

        urlschmes = []
        if plist_filename == '':
            self.errors.append('Info.plist file not found in IPA')
        else:
            content = zip_obj.read(plist_filename)
            data = plistlib.readPlistFromString(content)
            urltypes = data['CFBundleURLTypes']
            urlschemes = urltypes[0]['CFBundleURLSchemes']

        return urlschemes

if __name__ == '__main__':
    test_file_path = r'/Users/Ruozi/Music/iTunes/iTunes Media/Mobile Applications/SketchBook 3.1.2.ipa'
    getter = GetSchemeUrl(test_file_path)
    print getter.extract_scheme_url()
        
    sys.exit(0)


