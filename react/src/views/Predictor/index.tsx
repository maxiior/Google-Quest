import { useState } from "react";
import "./index.scss";
import LoadingIcon from "components/LoadingIcon";
import ErrorPanel from "components/ErrorPanel";
import { makePrediction } from "api/services/predictions.service";
import ResponsePanel from "components/ResponsePanel";

const Predictor = () => {
  const autoResizeTextarea = (e: any) => {
    e.target.style.height = "inherit";
    e.target.style.height = `${e.target.scrollHeight}px`;
  };
  const [pending, setPending] = useState(false);

  const [questionTitle, setquestionTitle] = useState("");
  const [questionBody, setquestionBody] = useState("");
  const [answer, setAnswer] = useState("");
  const [category, setCategory] = useState("");

  const [error, setError] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);
  const [response, setResponse] = useState(false);

  const makePredictionProcess = () => {
    setError(false);
    setShowAnswer(false);
    setPending(true);

    makePrediction({
      question_title: questionTitle,
      question_body: questionBody,
      answer: answer,
      category: category,
    })
      .then((response) => {
        if (response.status === 200) {
          setPending(false);
          setShowAnswer(true);
          setResponse(response.data);
        }
      })
      .catch(() => {
        setPending(false);
        setError(true);
      });
  };

  return (
    <div>
      {error && <ErrorPanel />}
      <textarea
        placeholder="question title"
        className="textarea"
        onChange={(e) => {
          autoResizeTextarea(e);
          setquestionTitle(e.target.value);
          setError(false);
        }}
      />
      <textarea
        placeholder="question body"
        className="textarea"
        onChange={(e) => {
          autoResizeTextarea(e);
          setquestionBody(e.target.value);
          setError(false);
        }}
      />
      <textarea
        placeholder="answer"
        className="textarea"
        onChange={(e) => {
          autoResizeTextarea(e);
          setAnswer(e.target.value);
          setError(false);
        }}
      />
      <textarea
        placeholder="category"
        className="textarea"
        onChange={(e) => {
          autoResizeTextarea(e);
          setCategory(e.target.value);
          setError(false);
        }}
      />
      {!pending ? (
        <button className="button" onClick={() => makePredictionProcess()}>
          Send
        </button>
      ) : (
        <div className="icon-holder">
          <LoadingIcon />
        </div>
      )}
      {showAnswer && <ResponsePanel response={response} />}
    </div>
  );
};

export default Predictor;
