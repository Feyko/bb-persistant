import buildbot_worker
import pyqrcode


def to_ascii_qr_code(text: str) -> str:
    qr = pyqrcode.create(text)
    return qr.terminal()


if __name__ == '__main__':
    version = buildbot_worker.version
    qrcode = to_ascii_qr_code(version)
    print(qrcode)
