(function () {
    'use strict';

    var app = angular.module('signup-factory', []);

    app.factory('SignupLabel', function () {
        var Label = {
            label_signup_title : function () {
                return 'Registre-se';
            },
            label_full_name: function () {
                return 'Nome Completo';
            },
            label_email : function () {
                return 'E-mail';
            },
            label_password : function () {
                return 'Senha';
            },
            label_confirm_password : function () {
                return 'Confirmar Senha';
            },
            label_cpf : function () {
                return 'CPF';
            }
        };

        return Label;
    });

    app.factory('EventUrls', function () {
        var EventUrls = {
            spots_event_available : function (event_id) {
                return '/event/' + event_id + '/spots_event_available/';
            },
            spots_session_available: function (session_id) {
                return '/session/' + session_id + '/spots_session_available/';
            },
        };

        return EventUrls;
    });

})(window.angular);