# Generated by Django 4.1.7 on 2023-05-12 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_asker_intent_understanding', models.FloatField(default=0)),
                ('question_body_critical', models.FloatField(default=0)),
                ('question_conversational', models.FloatField(default=0)),
                ('question_expect_short_answer', models.FloatField(default=0)),
                ('question_fact_seeking', models.FloatField(default=0)),
                ('question_has_commonly_accepted_answer', models.FloatField(default=0)),
                ('question_interestingness_others', models.FloatField(default=0)),
                ('question_interestingness_self', models.FloatField(default=0)),
                ('question_multi_intent', models.FloatField(default=0)),
                ('question_not_really_a_question', models.FloatField(default=0)),
                ('question_opinion_seeking', models.FloatField(default=0)),
                ('question_type_choice', models.FloatField(default=0)),
                ('question_type_compare', models.FloatField(default=0)),
                ('question_type_consequence', models.FloatField(default=0)),
                ('question_type_definition', models.FloatField(default=0)),
                ('question_type_entity', models.FloatField(default=0)),
                ('question_type_instructions', models.FloatField(default=0)),
                ('question_type_procedure', models.FloatField(default=0)),
                ('question_type_reason_explanation', models.FloatField(default=0)),
                ('question_type_spelling', models.FloatField(default=0)),
                ('question_well_written', models.FloatField(default=0)),
                ('answer_helpful', models.FloatField(default=0)),
                ('answer_level_of_information', models.FloatField(default=0)),
                ('answer_plausible', models.FloatField(default=0)),
                ('answer_relevance', models.FloatField(default=0)),
                ('answer_satisfaction', models.FloatField(default=0)),
                ('answer_type_instructions', models.FloatField(default=0)),
                ('answer_type_procedure', models.FloatField(default=0)),
                ('answer_type_reason_explanation', models.FloatField(default=0)),
                ('answer_well_writte', models.FloatField(default=0)),
            ],
        ),
    ]