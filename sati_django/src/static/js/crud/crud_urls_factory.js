(function () {
    'use strict';

    var app = angular.module('crud-urls-factory', []);

    app.factory('Urls', function () {
        var Urls = {
            event: function () {
                return '/api/event/';
            },
            category: function () {
                return '/api/category/';
            },
            session: function () {
                return '/api/session/';
            },
            edition: function () {
                return '/api/edition/';
            },
            room: function () {
                return '/api/room/';
            },
            person: function () {
                return '/api/public_person/';
            },
            api_person: function () {
                return '/api/person/';
            },

            // Get event by id and all events
            get_all_events: function () {
                return '/event/get_all_events/';
            },
            get_event: function (id_event) {
                return '/event/'+ id_event +'/get_event/';
            },

            // Get all sessions
            get_all_sessions: function () {
                return '/session/get_all/';
            },

            add_new_participant : function () {
                return '/user_signup/';
            },
            get_sessions_user : function () {
                return '/get_sessions_user/';
            },
            get_all_participants : function () {
                return Urls.dashboard() +  'get_all_participants/';
            },
            update_participant : function () {
                return '/update_participant/';
            },
            confirm_participant : function () {
                return Urls.dashboard() + 'confirm_participant/';
            },
            dashboard :function () {
                return '/dashboard/'
            },
            // Login
            login : function () {
                return '/user_login/';
            }
        };

        return Urls;
    });

})(window.angular);

/*

<img src="{[{ event.category.image }]}" alt="" />


    */