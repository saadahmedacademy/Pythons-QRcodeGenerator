import qrcode  # type: ignore
from PIL import Image # type: ignore

qr = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,)

qr.add_data('https://www.linkedin.com/in/saad-azeem-a74a04273/?trk=li_LOL_SPIN_global_careers_jobsgtm_otw2_acq_Nov2020_spinv4')
qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
img.save('linkedin.png')

