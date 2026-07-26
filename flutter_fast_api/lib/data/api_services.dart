import 'dart:developer';

import 'package:dio/dio.dart';
import 'package:flutter_fast_api/data/sharedpreference_helper.dart';
import 'package:flutter_fast_api/model/book_list_model.dart';
import 'package:flutter_fast_api/model/login_response.dart';

class BookApiService {
  final String baseUrl = "https://fast-api-project-z7yg.onrender.com/";
  // final String baseUrl = "http://127.0.0.1:8000/";
  final _dio = Dio();

  Future<AuthResponse> login(String username, String password) async {
    try {
      log("api endpoint: ${baseUrl}auth/login");

      final response = await _dio.post(
        '${baseUrl}auth/login',
        options: Options(contentType: Headers.jsonContentType),
        data: {'email': username, 'password': password},
      );
      log("response: ${response.data}");

      if (response.statusCode == 200) {
        final authResponseModel = AuthResponse.fromJson(response.data);
        await LocalStorageHelper.saveToken(
          authResponseModel.accessToken,
          authResponseModel.tokenType,
        );
        await LocalStorageHelper.saveUser(authResponseModel.user);
        return authResponseModel;
      }
      throw Exception('Login failed: ${response.statusCode}');
    } on DioException catch (e) {
      if (e.response?.statusCode == 401) {
        throw Exception('Invalid username or password');
      }
      throw Exception('Login error: ${e.message}');
    }
  }

  Future<void> signup({
    required String username,
    required String email,
    required String password,
    required String role,
  }) async {
    try {
      log("api endpoint: ${baseUrl}auth/signup");

      final response = await _dio.post(
        '${baseUrl}auth/signup',
        options: Options(contentType: Headers.jsonContentType),
        data: {
          "username": username,
          "email": email,
          "password": password,
          "role": role,
        },
      );

      log("response: ${response.data}");

      if (response.statusCode == 200 || response.statusCode == 201) {
        return;
      }

      throw Exception(response.data["message"] ?? "Signup failed");
    } on DioException catch (e) {
      if (e.response != null) {
        final data = e.response!.data;

        if (data is Map<String, dynamic>) {
          throw Exception(data["detail"] ?? data["message"] ?? "Signup failed");
        }
      }

      throw Exception("Signup error: ${e.message}");
    }
  }

  Future<AuthResponse> verifyOtp({
    required String email,
    required String otp,
  }) async {
    try {
      final response = await _dio.post(
        '${baseUrl}auth/verify-otp',
        data: {"email": email, "otp": otp},
      );

      return AuthResponse.fromJson(response.data);
    } on DioException catch (e) {
      throw Exception(e.response?.data["detail"] ?? "OTP verification failed");
    }
  }

  Future<void> resendOtp(String email) async {
    try {
      await _dio.post('${baseUrl}auth/resend-otp', data: {"email": email});
    } on DioException catch (e) {
      throw Exception(e.response?.data["detail"] ?? "Unable to resend OTP");
    }
  }

  Future<Options> _authorizedOptions() async {
    final token = await LocalStorageHelper.getToken();

    if (token == null || token.isEmpty) {
      throw Exception("User is not logged in.");
    }

    return Options(
      headers: {
        "Authorization": "Bearer $token",
        "Content-Type": Headers.jsonContentType,
      },
    );
  }

  Future<List<BookListResponse>> getBooks() async {
    try {
      log("api endpoint: ${baseUrl}books/get_books");
      final response = await _dio.get(
        '${baseUrl}books/get_books',
        options: await _authorizedOptions(),
      );
      log("response: ${response.data}");
      if (response.statusCode == 200) {
        final List<dynamic> data = response.data;
        return data.map((json) => BookListResponse.fromJson(json)).toList();
      }
      throw Exception('Failed to load books: ${response.statusCode}');
    } on DioException catch (e) {
      throw Exception('Network error: ${e.message}');
    }
  }

  Future<bool> deleteBook(int bookId) async {
    try {
      log("api endpoint: ${baseUrl}books/delete_book/$bookId");
      final response = await _dio.delete(
        '${baseUrl}books/delete_book/$bookId',
        options: await _authorizedOptions(),
      );
      log("response: ${response.data}");
      return response.statusCode == 200 || response.statusCode == 204;
    } on DioException catch (e) {
      throw Exception('Failed to delete book: ${e.message}');
    }
  }

  Future<BookListResponse> updateBook(int bookId, BookListResponse book) async {
    try {
      log("api endpoint: ${baseUrl}books/update_book/$bookId");
      final response = await _dio.put(
        '${baseUrl}books/update_book/$bookId',
        options: await _authorizedOptions(),
        data: {
          'title': book.title,
          'description': book.description,
          'author': book.author,
          'year': book.year,
        },
      );
      log("response: ${response.data}");

      if (response.statusCode == 200) {
        return BookListResponse.fromJson(response.data);
      }
      throw Exception('Failed to update book');
    } on DioException catch (e) {
      throw Exception('Failed to update book: ${e.message}');
    }
  }

  Future<BookListResponse> createBook(BookListResponse book) async {
    try {
      log("api endpoint: ${baseUrl}books/create_book");
      final response = await _dio.post(
        '${baseUrl}books/create_book',
        options: await _authorizedOptions(),
        data: {
          'title': book.title,
          'description': book.description,
          'author_id': book.authorId,
          'author': book.author,
          'year': book.year,
        },
      );
      log("response: ${response.data}");

      if (response.statusCode == 200 || response.statusCode == 201) {
        return BookListResponse.fromJson(response.data);
      }
      throw Exception('Failed to create book');
    } on DioException catch (e) {
      throw Exception('Failed to create book: ${e.message}');
    }
  }
}
