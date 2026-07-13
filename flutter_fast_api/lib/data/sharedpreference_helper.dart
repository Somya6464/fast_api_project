import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

import '../model/login_response.dart';

class LocalStorageHelper {
  static const _tokenKey = 'access_token';
  static const _tokenTypeKey = 'token_type';
  static const String _userKey = "user";

  /// Save token after login
  static Future<void> saveToken(String accessToken, String tokenType) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_tokenKey, accessToken);
    await prefs.setString(_tokenTypeKey, tokenType);
  }

  /// Get stored token (returns null if not logged in)
  static Future<String?> getToken() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString(_tokenKey);
  }

  static Future<void> saveUser(UserModel user) async {
    final prefs = await SharedPreferences.getInstance();

    await prefs.setString(_userKey, jsonEncode(user.toJson()));
  }

  static Future<UserModel?> getUser() async {
    final prefs = await SharedPreferences.getInstance();

    final user = prefs.getString(_userKey);

    if (user == null) return null;

    return UserModel.fromJson(jsonDecode(user));
  }


  /// Get token type (e.g., "bearer")
  static Future<String?> getTokenType() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString(_tokenTypeKey);
  }

  /// Check if user is logged in
  static Future<bool> isLoggedIn() async {
    final token = await getToken();
    return token != null && token.isNotEmpty;
  }

  /// Clear token on logout
  static Future<void> clearToken() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_tokenKey);
    await prefs.remove(_tokenTypeKey);
    await prefs.remove(_userKey);
  }
}
