import os

import astromatic_wrapper as aw


def sextractor(result_path, img_path):
    cat_name = os.path.basename(img_path).replace('.fits', '.ldac.fits')
    cat_path = os.path.join(result_path, cat_name)

    kwargs = {
        'code': 'SExtractor',
        'config': {
            'CATALOG_NAME': cat_path,
            'CATALOG_TYPE': 'FITS_LDAC',
            'FILTER': False,
        },
        'temp_path': 'result',
        'params': ['NUMBER',
                   'XWIN_IMAGE', 'YWIN_IMAGE',
                   'XWIN_WORLD', 'YWIN_WORLD',
                   'ERRAWIN_IMAGE', 'ERRBWIN_IMAGE', 'ERRTHETAWIN_IMAGE',
                   'FLUX_AUTO', 'FLUXERR_AUTO', 'FLUX_RADIUS',
                   'EXT_NUMBER', 'ELONGATION',
                   ],
    }
    wrapper = aw.api.Astromatic(**kwargs)
    wrapper.run(img_path)
    return cat_path


def scamp(result_path, cat_path):
    kwargs = {
        'code': 'SCAMP',
        'config': {
            'REF_SERVER': 'vizier.china-vo.org',
            'ASTREF_CATALOG': 'GAIA-DR2',
            'ASTREF_BAND': 'DEFAULT',
            'SOLVE_PHOTOM': 'N',
            'CHECKPLOT_DEV': 'PNG',
        },
    }
    wrapper = aw.api.Astromatic(**kwargs)
    wrapper.run(cat_path)
    return 0


if __name__ == "__main__":
    fits_path = 'test.fit'
    cat_path = sextractor('result', fits_path)
    result = scamp('result', cat_path)