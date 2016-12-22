(function () {
    'use strict';

    var app = angular.module('sati-factory', ['ngMaterial', 'ngMessages', 'material.svgAssetsCache']);


    /* -- Toast -- */
    var isDlgOpen;

    app.controller('ToastCtrl', function($scope, $mdToast, $mdDialog, $log, message) {
        $scope.text = message;

        $scope.closeToast = function() {

            if (isDlgOpen) return;
            $mdToast.hide().then(function() {
                isDlgOpen = false;
            });
      };
    });

    app.factory('Toast', function ($mdToast) {

        var Toast = {
            showToast : function(text) {
                $mdToast.show({
                    hideDelay   : 5000,
                    position    : 'top left right',
                    locals: {message: text},
                    controller  : 'ToastCtrl',
                    controllerAs : 'toastCtrl',
                    templateUrl : '/static/templates/sati/toast.html'
                });
            }
        };

        return Toast;

    });

    app.factory('Addons', function ($log, ConvertFieldLabel) {
        var Addon = {
            toggle : function (item, list) {
                var idx = list.indexOf(item);
                if (idx > -1) {
                    list.splice(idx, 1);
                }
                else {
                    list.push(item);
                }
            },
            exists : function (item, list) {
                    return list.indexOf(item) > -1;
            },
            convertFields : function (items) {
                var newItems = [];

                angular.forEach(items, function (value, key) {
                    var new_item = {};
                    new_item.name = ConvertFieldLabel(key);
                    new_item.message = value;

                    newItems.push(new_item);
                });



                return newItems;
            }

        };
        return Addon;
    });


    app.factory('Label', function () {
        var Label = {
            tbd: function () {
                return 'A definir';
            },
            no_results: function () {
                return 'Nenhum resultado encontrado.';
            },
            clear_filter: function () {
                return 'Limpar Filtro';
            },
            none: function () {
                return 'Nenhum';
            },
            until: function () {
                return ' até ';
            },
            at: function () {
                return ' ás ';
            },
            by: function () {
                return ' por ';
            },
            open_sessions : function () {
                return 'Turmas Abertas';
            },
            sessions : function () {
                return 'Turmas';
            },
            no_spot : function () {
                return 'Esgotado';
            },
            occurence: function () {
                return 'Cronograma';
            },
            label_event_name : function () {
              return 'Nome do Evento';
            },
            label_person_name : function () {
                return 'Nome Completo';
            },
            label_person_cpf : function () {
                return 'CPF';
            },
            label_person_academic_registry : function () {
                return 'Registro Acadêmico';
            },
            label_participant_confirmed : function () {
                return 'Confirmação';
            },
            label_participants : function () {
                return 'Participantes';
            },
            label_participant_is_confimed_true : function () {
                return 'Confirmado(a)';
            },
            label_participant_is_confimed_false : function () {
                return 'Não Confirmado(a)';
            },
            label_participant_is_confimed_true_lower : function () {
                return 'confirmada';
            },
            label_participant_is_confimed_false_lower : function () {
                return 'não confirmada';
            },

            // Lista
            title_table_confirm_participation: function () {
                return 'Lista de participações modificadas'
            },

            // Label Button
            label_button_confirm_participation : function () {
                return 'Confirmar Participações';
            },

            // Buttons
            back_top: function () {
                return 'Voltar pro Topo';
            },
            button_close : function () {
                return 'Fechar';
            },
            button_save : function () {
                return 'Salvar';
            },
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
            label_confirm : function () {
              return "confirmado"
            },
            label_already_registered : function () {
              return "cadastrado anteriormente"
            },

            // error
            error_name: function () {
              return 'Nome';
            },
            label_sessions: function () {
              return 'Turma';
            },
            label_login: function () {
              return 'Login';
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
            // filter
            filters : function () {
              return 'Filtros';
            },
            filter_label_event_category: function () {
                return 'Categoria';
            },
            filter_label_participant_name: function () {
                return 'Nome do Participante';
            },

        };

        return Label;
    });


})(window.angular);