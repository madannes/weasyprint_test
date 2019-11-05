import logging
import settings
from weasyprint import HTML

logger = logging.getLogger(settings.STANDARD_LOGGER)

logger.info('Starting up...')

for i in range(0, 1):
    html = HTML('templates/test.html')
    html.write_pdf(f'templates/output/test{i + 1}.pdf')

logger.info('Success!')
