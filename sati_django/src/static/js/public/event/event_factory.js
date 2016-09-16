(function () {
    'use strict';

    var app = angular.module('event-factory', []);

    app.factory('EventLabel', function () {
        var Label = {
            filter_label_event_name : function () {
                return 'Nome do Evento';
            },
            filter_label_filter_event : function () {
                return 'Encontre Eventos';
            },
            filter_label_event_begin_date : function () {
                return 'Eventos até';
            },
            filter_label_event_category: function () {
                return 'Categoria';
            },
            no_results_session : function () {
                return 'Nenhuma turma disponível';

            },
            no_results_occurrence : function () {
                return 'Nenhuma ocorrência disponível';
            }
        };

        return Label;
    });

    app.factory('EventUrls', function () {
        var EventUrls = {
            spots_event : function (event_id) {
                return '/event/spots_event/' + event_id + '/';
            },
            spots_session: function () {
                return 'event/spots_session/';
            },
            spots_session_available: function () {
                return 'event/spots_session_available/';
            },
        };

        return EventUrls;
    });

})(window.angular);