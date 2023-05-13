import React, { useEffect, useState } from "react";
import ResponsePanel from "components/ResponsePanel";
import { getPredictions } from "api/services/predictions.service";
import LoadingIcon from "components/LoadingIcon";
import ErrorPanel from "components/ErrorPanel";
import "./index.scss";

const Predictions = () => {
  const [error, setError] = useState(false);
  const [pending, setPending] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);
  const [response, setResponse]: any = useState(false);

  useEffect(() => {
    setPending(true);
    getPredictions()
      .then((response) => {
        if (response.status === 200) {
          setPending(false);
          setShowAnswer(true);
          console.log(response.data);
          setResponse(response.data);
        }
      })
      .catch(() => {
        setPending(false);
        setError(true);
      });
  }, []);

  var rows: any = [];

  if (response) {
    response.forEach((i: any) => {
      rows.push(
        <div className="margin">
          <ResponsePanel response={i} />
        </div>
      );
    });
  }

  return (
    <div>
      {error && <ErrorPanel />}
      {pending ? (
        <div className="icon-holder">
          <LoadingIcon />
        </div>
      ) : (
        <>{rows}</>
      )}
    </div>
  );
};

export default Predictions;
