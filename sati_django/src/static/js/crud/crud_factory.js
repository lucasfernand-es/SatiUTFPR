(function () {
    'use strict';

    var app = angular.module('crud-factory', [ 'crud-urls-factory'
                                        ]);

    app.factory('ModelUtils', function($http, $log) {


        var handleErrors =  function(serverResponse, status, errorDestination) {
            if (angular.isDefined(errorDestination)) {
                if (status >= 500) {
                    errorDestination.form = 'Server Error: ' + status;
                } else if (status >= 401) {
                    errorDestination.form = 'Unauthorized Error: ' + status;
                } else {
                    angular.forEach(serverResponse, function(value, key) {
                        if (key != '__all__') {
                            errorDestination[key] = angular.isArray(value) ? value.join("<br/>") : value;
                        } else {
                            errorDestination.form = errorDestination.form || '' + key + ':' + angular.isArray(value) ? value.join("<br/>") : value;
                        }
                    });
                }
            }
        };

        var auth = {params:{"source":"angular"}};

        var ModelUtils = {
            get_request: function(url) {
                return $http.get(url, auth).then(function(response){
                        return response.data;
                    }
                );
            },
            get: function(url, id) {
                return $http.get(url + id + '/', auth).then(function(response){
                        //$log.log('get');
                        //$log.log(response.data);
                        return response.data;
                    }
                );
            },

            get_all: function(url) {
                return $http.get(url, auth).then(function(response){
                        //$log.log('get');
                        //$log.log(response.data);
                        return response.data;
                    }
                );
            },

            post_request: function(url, obj, errors) {
                //$log.log(obj);

                return $http.post(url, obj, auth).
                    success(function(response, status, headers, config) {
                        //$log.log('response');
                        //$log.log(response);
                        return response.data;
                        angular.extend(obj, response);
                    }).
                    error(function(response, status, headers, config) {
                        handleErrors(response, status, errors);
                    });
            },

            create: function(url, obj, errors) {
                $log.log(obj);
                return $http.post(url, obj).
                    success(function(response, status, headers, config) {
                        //$log.log(response);
                        angular.extend(obj, response);
                    }).
                    error(function(response, status, headers, config) {
                        $log.log(response);
                        handleErrors(response, status, errors);
                    });
            },

            save: function(url, obj, errors) {
                $log.log(obj);
                if (angular.isDefined(obj.id)) {
                    return $http.put(url + obj.id + '/', obj).
                            success(function(response, status, headers, config) {
                                angular.extend(obj, response);
                            }).
                            error(function(response, status, headers, config) {
                                $log.log(errors);
                                handleErrors(response, status, errors);
                            });
                } else {
                    return this.create(url, obj, errors);
                }
            },

            del: function(url, obj) {
                return $http.delete(url + obj.id + '/');
            }
        };

        return ModelUtils;

    });

    app.factory('ConvertFieldLabel', function (CRUDLabel) {
        var ConvertFieldLabel = function (key) {
            switch (key) {
                case 'name' : return CRUDLabel.error_name();
                case 'password' : return CRUDLabel.label_password();
                case 'confirm_password' : return CRUDLabel.label_confirm_password();
                case 'email' : return CRUDLabel.label_email();
                case 'academic_registry': return CRUDLabel.label_academic_registry();
                case 'cpf': return CRUDLabel.label_cpf();
                case 'role': return CRUDLabel.label_role();
                case 'institution': return CRUDLabel.label_institution();
                case 'sessions': return CRUDLabel.label_sessions();
                case 'errors': return 'Erro(s) Detectado(s): ';

                default: return key;
            };


        };

        return ConvertFieldLabel;
    });


    app.factory('CRUDLabel', function () {
        var CRUDLabel = {
            label_login_title : function () {
                return 'Entrar';
            },
            label_login_button : function () {
                return 'Log in';
            },

            // main
            label_insert_error : function () {
              return "Erro(s) detectado(s):"
            },
            label_insert_success : function () {
              return "Sucesso!"
            },

            // error
            error_name: function () {
              return 'Nome';
            },
            label_sessions: function () {
              return 'Turma';
            },

            // Filters
            filter_label_event_name : function () {
                return 'Nome do Evento';
            },
            filter_label_category: function () {
                return 'Categoria';
            },
            // Person
            label_role: function () {
                return 'Cargo'
            },
            label_add_item: function () {
                return 'Cadastrar';
            },
            label_clear: function () {
                return 'Limpar';
            },

            label_person_full_name: function () {
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
            },
            label_academic_registry : function () {
                return 'Registro Acadêmico';
            },
            label_occurrence : function () {
                return 'Cronograma:';
            },
            label_institution : function () {
                return 'Instituição';
            },

            // event
            label_event : function () {
                return 'Evento';
            },
            label_participation : function () {
                return 'Participação';
            },
            label_person : function () {
                return 'Participante';
            },

            // Forms
            label_required_field_error : function () {
                return 'Este campo não pode ser em branco.';
            },
            label_valid_email_error : function () {
                return 'Insira um endereço de email válido.';
            },
            label_password_match_error : function () {
                return 'As senhas informadas devem ser iguas.';
            },
            label_valid_cpf_error : function () {
                return 'Insira um número de CPF válido.';
            },
        };

        return CRUDLabel;
    });

    app.factory('FieldSize', function () {

        var textFieldSize = function (number) {
            return "Certifique-se de que este campo não tenha mais de "+ number +" caracteres.";
        };

        var FieldSize = {
            name: function () {
                return 255;
            },
            name_error: function () {
                return textFieldSize(FieldSize.name());
            },
            email: function () {
                return 100;
            },
            email_error: function () {
                return textFieldSize(FieldSize.email());
            },
            cpf: function () {
                return 15;
            },
            cpf_error: function () {
                return textFieldSize(FieldSize.cpf());
            },
            academic_registry: function () {
                return 15;
            },
            academic_registry_error: function () {
                return textFieldSize(FieldSize.academic_registry());
            },
            password: function () {
                return 32;
            },
            password_error: function () {
                return textFieldSize(FieldSize.password());
            },
        };

        return FieldSize;
    });

})(window.angular);
