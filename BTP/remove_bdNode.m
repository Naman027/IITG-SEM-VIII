function intNodeIndex = remove_bdNode(node, T)
    bdFace = double(T.bdFace);
    [bdNode, ~, ~] = myunique(bdFace(:));
    N = size(node, 1);
    allNode = (1:N)';
    intNodeIndex = allNode(~ismember(allNode, bdNode));
end

