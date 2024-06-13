# Application Server

This project demonstrates setting up a Flask application served via Gunicorn and Nginx. It includes development and production environments for serving a simple "Hello HBNB!" page, handling dynamic routes, and deploying a RESTful API and dynamic website.

## Files

- `web_flask/0-hello_route.py`: Flask application for serving the "Hello HBNB!" page.
- `gunicorn.service`: Systemd service configuration for Gunicorn.
- `2-app_server-nginx_config`: Nginx configuration for serving Flask app via Gunicorn.
- `3-app_server-nginx_config`: Nginx configuration for serving Flask app with dynamic routes via Gunicorn.
- `4-app_server-nginx_config`: Nginx configuration for serving RESTful API via Gunicorn.
- `5-app_server-nginx_config`: Nginx configuration for serving dynamic website via Gunicorn.
- `4-reload_gunicorn_no_downtime`: Bash script to reload Gunicorn without downtime.

## Installation

1. **Install Dependencies**:
    ```sh
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv nginx gunicorn tmux
    ```

2. **Clone Repositories**:
    ```sh
    git clone https://github.com/yourusername/AirBnB_clone_v2.git
    git clone https://github.com/yourusername/AirBnB_clone_v3.git
    git clone https://github.com/yourusername/AirBnB_clone_v4.git
    ```

3. **Set Up Flask Application**:
    ```sh
    cd AirBnB_clone_v2
    vim web_flask/0-hello_route.py
    ```

## Usage

- **Development**:
    ```sh
    python3 -m web_flask.0-hello_route
    ```

- **Production**:
    ```sh
    gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
    ```

## Nginx Configuration

1. **Basic Configuration**:
    ```sh
    vim 2-app_server-nginx_config
    ```

2. **Dynamic Route Configuration**:
    ```sh
    vim 3-app_server-nginx_config
    ```

3. **API Configuration**:
    ```sh
    vim 4-app_server-nginx_config
    ```

4. **Dynamic Website Configuration**:
    ```sh
    vim 5-app_server-nginx_config
    ```

## Systemd Service

- **Gunicorn Service**:
    ```sh
    vim gunicorn.service
    sudo systemctl start gunicorn
    sudo systemctl enable gunicorn
    ```

## Bash Script

- **Reload Gunicorn**:
    ```sh
    vim 4-reload_gunicorn_no_downtime
    chmod +x 4-reload_gunicorn_no_downtime
    ```

## Testing

- **Development**:
    ```sh
    curl 127.0.0.1:5000/airbnb-onepage/
    ```

- **Production**:
    ```sh
    curl 127.0.0.1/airbnb-onepage/
    ```

## Expected Output

- **Hello HBNB!**

