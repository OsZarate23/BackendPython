from flask import jsonify


class FlaskInterceptors:
    @staticmethod
    def handle_400_error(error):
        return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

    @staticmethod
    def handle_404_error(error):
        return jsonify({'error': 'Not Found', 'message': str(error)}), 404

    @staticmethod
    def handle_500_error(error):
        return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500

    @staticmethod
    def before_request():
        # Lógica a ejecutar antes de cada solicitud
        print("Interceptando antes de la solicitud")

    @staticmethod
    def after_request(response):
        # Modificar la respuesta si es necesario
        response.headers['X-Custom-Header'] = 'MiValorPersonalizado'
        print("Interceptando después de la solicitud")
        return response
