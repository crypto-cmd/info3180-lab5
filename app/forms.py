from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class MovieForm(FlaskForm):
	title = StringField(
		"Movie Title",
		validators=[
			DataRequired(message="Movie title is required."),
			Length(max=255, message="Movie title must be 255 characters or fewer."),
		],
	)
	description = TextAreaField(
		"Description",
		validators=[
			DataRequired(message="A brief movie description is required."),
			Length(
				min=10,
				max=1000,
				message="Description must be between 10 and 1000 characters.",
			),
		],
	)
	poster = FileField(
		"Poster",
		validators=[
			FileRequired(message="A movie poster image is required."),
			FileAllowed(
				["jpg", "jpeg", "png", "gif", "webp"],
				message="Only image files (jpg, jpeg, png, gif, webp) are allowed.",
			),
		],
	)