(function () {
    'use strict';

    var app = angular.module('crud-factory', [
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

        var ModelUtils = {
            get: function(url, id) {
                $http.get(url + id + '/').then(function(response){response.data});
            },

            create: function(url, obj, errors) {
                $log.log(obj);
                obj.important = true;

                return $http.post(url, obj).
                    success(function(response, status, headers, config) {
                        angular.extend(obj, response);
                    }).
                    error(function(response, status, headers, config) {
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

})(window.angular);
