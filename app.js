var app = angular.module('plunker', ['ngRoute']);

app.config(function($routeProvider) {
    $routeProvider
    .when('/', {
        controller: 'homeController',
        template: '<h2>Home</h2>'
    })
    .when('/about', {
        controller: 'aboutController',
        templateUrl: 'about.html'
    })
    .when('/music', {
        controller: 'musicController',
        templateUrl: 'music.html'
    })
    .otherwise({
        controller: '404Controller',
        templateUrl: '404.html'
    });
});

app.controller('appController', function($scope, $location) {
    $scope.isActive = function(path) {
        return $location.path() === path;
    };
});

app.controller('homeController', function($scope) {});

app.controller('aboutController', function($scope) {});

app.controller('404Controller', function($scope, $location) {
    $scope.path = $location.path();
    $scope.back = function() {
        history.back();
    };
});