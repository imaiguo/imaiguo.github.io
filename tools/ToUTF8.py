
import os
import time
import loguru
import codecs
import chardet

# 检验文本文件的编码格式并转为utf-8
def GBKToUTF8(filepath, targetpath, targetCode="UTF-8"):
    try:
        content = open(filepath, 'rb').read()
        source_encoding = chardet.detect(content)
        curCoding = source_encoding['encoding']
        loguru.logger.info(f"当前文件编码格式 ->[{curCoding}] [{filepath}]")

        if(curCoding != "utf-8"):
            if(curCoding == 'GB2312'):
                # GB2312、GBK、GB18030是兼容的 包含的字符个数: GB2312 < GBK < GB18030
                content = content.decode("GB18030")
                content = content.encode(targetCode)
                codecs.open(targetpath, 'wb').write(content)
            else:
                content = content.decode(source_encoding['encoding']).encode(targetCode)
                codecs.open(targetpath, 'wb').write(content)
            loguru.logger.debug(f"转换完成 [{filepath}] -> [{targetpath}]")
        else:
            loguru.logger.debug("无需转换")

    except IOError as err:
        loguru.logger.error("I/O error:{0}".format(err))

def ScanDirTransfer(dirpath):
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            splite = os.path.splitext(file)[1]
            if splite == '.html' or splite == '.htm':
                path = os.path.join(root, file)
                loguru.logger.debug(f"开始处理文件-> [{path}]")
                GBKToUTF8(path, path)

if __name__ == "__main__":
    # RunMain()

    path = "/opt/www/html/b/s3"
    ScanDirTransfer(path)

    # sourcePath  = "/opt/www/html/tools/index.html"
    # # sourcePath = "/opt/www/html/b/s3/002/2213国度/017第十六章　长大、变化和建造的收成.htm"
    # targetPath = "/opt/www/html/tools/index_utf8.html"
    # GBKToUTF8(sourcePath, targetPath)

