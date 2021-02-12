import logging
from weasyprint import HTML

logger = logging.getLogger('weasyprint_test')

logger.info('Starting up...')

for i in range(0, 3):
    html = HTML('templates/test.html')
    html.write_pdf(f'templates/output/test{i + 1}.pdf')

logger.info('Success!')
