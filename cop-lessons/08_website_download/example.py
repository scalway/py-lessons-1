from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
import json
import time
from urllib.parse import urlparse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# placeholder analyzer - real implementation will be provided by user later
def analyze_page(html_text, url):
    """Placeholder analysis function. Returns a dict that will be saved as JSON.
    The user will replace this implementation later with real analysis logic.
    """
    return {
        'url': url,
        'length': len(html_text) if html_text is not None else 0,
        'fetched_at': time.time(),
        'notes': 'This is a placeholder analysis. Replace analyze_page with real logic.'
    }

@app.route('/')
def index():
    """Home page with form to submit a URL."""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form.get('url')
    if not url:
        flash('Proszę podać URL', 'error')
        return redirect(url_for('index'))

    # basic URL validation
    parsed = urlparse(url)
    if parsed.scheme not in ('http', 'https') or not parsed.netloc:
        flash('Nieprawidłowy URL. Upewnij się, że zaczyna się od http:// lub https://', 'error')
        return redirect(url_for('index'))

    # download page (simple implementation using requests)
    try:
        import requests
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        flash(f'Błąd podczas pobierania strony: {e}', 'error')
        return redirect(url_for('index'))

    # analyze page (user will replace analyze_page implementation later)
    result = analyze_page(html, url)

    # generate safe filename
    timestamp = int(time.time())
    safe_netloc = parsed.netloc.replace(':', '_')
    filename = f"analysis_{safe_netloc}_{timestamp}.json"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # save JSON
    try:
        with open(filepath, 'w') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
    except Exception as e:
        flash(f'Błąd podczas zapisu pliku: {e}', 'error')
        return redirect(url_for('index'))

    return render_template('result.html', filename=filename)

@app.route('/output/<path:filename>')
def output_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)


if __name__ == '__main__':
    print("=" * 50)
    print("FLASK APPLICATION STARTING")
    print("=" * 50)
    print("\nAvailable routes:")
    print("  - http://localhost:5000/")
    print("\n" + "=" * 50)

    app.run(debug=True, host='0.0.0.0', port=5000)