import io
import buildbot_worker
import qrcode


def to_ascii_qr_code(text: str) -> str:
    qr = qrcode.QRCode()
    qr.add_data(text)
    out = io.StringIO()
    qr.print_ascii(out=out)
    out.seek(0)
    return out.read()


if __name__ == '__main__':
    version = buildbot_worker.version
    qrcode = to_ascii_qr_code(version)
    print(qrcode)
