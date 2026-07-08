import 'package:flutter/material.dart';
import 'package:flutter_fast_api/model/book_list_model.dart';

class BookForm extends StatefulWidget {
  final BookListResponse? initialBook;
  final void Function(BookListResponse book) onSubmit;
  final String submitLabel;

  const BookForm({
    super.key,
    this.initialBook,
    required this.onSubmit,
    this.submitLabel = 'Save',
  });

  @override
  State<BookForm> createState() => _BookFormState();
}

class _BookFormState extends State<BookForm> {
  late final TextEditingController _titleController;
  late final TextEditingController _authorController;
  late final TextEditingController _descriptionController;
  late final TextEditingController _yearController;
  final _formKey = GlobalKey<FormState>();

  bool get _isEditMode => widget.initialBook != null;

  @override
  void initState() {
    super.initState();
    _titleController = TextEditingController(
      text: widget.initialBook?.title ?? '',
    );
    _authorController = TextEditingController(
      text: widget.initialBook?.author ?? '',
    );
    _descriptionController = TextEditingController(
      text: widget.initialBook?.description ?? '',
    );
    _yearController = TextEditingController(
      text: widget.initialBook?.year.toString() ?? '',
    );
  }

  @override
  void dispose() {
    _titleController.dispose();
    _authorController.dispose();
    _descriptionController.dispose();
    _yearController.dispose();
    super.dispose();
  }

  void _handleSubmit() {
    if (_formKey.currentState!.validate()) {
      final book = BookListResponse(
        id: widget.initialBook?.id ?? 0,
        title: _titleController.text.trim(),
        author: _authorController.text.trim(),
        description: _descriptionController.text.trim(),
        year: int.parse(_yearController.text.trim()),
      );
      widget.onSubmit(book);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Padding(
            padding: const EdgeInsets.only(bottom: 16),
            child: Text(
              _isEditMode ? 'Edit Book' : 'Create New Book',
              style: const TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
                color: Colors.deepPurple,
              ),
            ),
          ),
          TextFormField(
            controller: _titleController,
            decoration: const InputDecoration(
              labelText: 'Title *',
              border: OutlineInputBorder(),
              prefixIcon: Icon(Icons.title),
            ),
            validator: (value) => value == null || value.trim().isEmpty
                ? 'Title is required'
                : null,
          ),
          const SizedBox(height: 12),
          TextFormField(
            controller: _authorController,
            decoration: const InputDecoration(
              labelText: 'Author *',
              border: OutlineInputBorder(),
              prefixIcon: Icon(Icons.person),
            ),
            validator: (value) => value == null || value.trim().isEmpty
                ? 'Author is required'
                : null,
          ),
          const SizedBox(height: 12),
          TextFormField(
            controller: _descriptionController,
            decoration: const InputDecoration(
              labelText: 'Description',
              border: OutlineInputBorder(),
              prefixIcon: Icon(Icons.description),
            ),
            maxLines: 3,
          ),
          const SizedBox(height: 12),
          TextFormField(
            controller: _yearController,
            decoration: const InputDecoration(
              labelText: 'Year *',
              border: OutlineInputBorder(),
              prefixIcon: Icon(Icons.calendar_today),
            ),
            keyboardType: TextInputType.number,
            validator: (value) {
              if (value == null || value.trim().isEmpty)
                return 'Year is required';
              final year = int.tryParse(value.trim());
              if (year == null) return 'Enter a valid year';
              if (year < 1000 || year > DateTime.now().year + 1) {
                return 'Enter a valid year';
              }
              return null;
            },
          ),
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: _handleSubmit,
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.deepPurple,
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(vertical: 14),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8),
              ),
            ),
            child: Text(
              widget.submitLabel,
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
            ),
          ),
        ],
      ),
    );
  }
}
