# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\Vlad\\Desktop\\OPArianG0ne\\1.py'],
             pathex=['C:\\Program Files (x86)\\Python36-32\\Scripts'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='1',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
