Upload any file quickly and conveniently to AnonFiles just using the command line

```
usage: anupload [-h] [--qr] [--direct] FILE [FILE ...]

Upload file to AnonFiles

positional arguments:
  FILE        file to upload

optional arguments:
  -h, --help  show this help message and exit
  --qr        gen QR code for every file
  --direct    get direct link to download
```

## Installing
Termux: `sh -c $(curl https://raw.githubusercontent.com/json1c/anonfiles-upload/master/termux_install.sh)`

Linux: `sh -c $(curl https://raw.githubusercontent.com/json1c/anonfiles-upload/master/linux_install.sh)`

### Example
`anupload file1.txt file2.txt`
